import xml.etree.ElementTree as et
import glob
import re
import pathlib
import argparse


INDENT = "    "
INPUT_DIR = "."
OUTPUT_DIR = "./out"

LOG_LEVEL_DEBUG = 0
LOG_LEVEL_INFO = 1
LOG_LEVEL_NOTICE = 2
LOG_LEVEL_WARN = 3
LOG_LEVEL_ERR = 4

LOG_LEVEL_LABEL = ["DEBUG", "INFO", "NOTICE", "WARN", "ERR"]

LOG_LEVEL = LOG_LEVEL_WARN


def output_log(level, message):
    if level >= LOG_LEVEL:
        print("[{0}] {1}".format(LOG_LEVEL_LABEL[level], message))


class BaseAnalyzer:
    def _analyze_paragraph(self, filename, elm):
        s = ""
        for text in elm.itertext():
            s = s + text
        return s

    def _analyze_list_item(self, filename, elm):
        for child in list(elm):
            if child.tag == "paragraph":
                ls = child.find("literal_strong")
                if ls:
                    return ls.text
                ls = child.find("strong")
                if ls:
                    return ls.text

        output_log(
            LOG_LEVEL_WARN,
            "<literal_strong> or <strong> is not found. "\
            "(filename={0})".format(filename)
        )

        return None

    def _analyze_bullet_list(self, filename, elm):
        items = []
        for child in list(elm):
            if child.tag == "list_item":
                items.append(self._analyze_list_item(filename, child))
        return items

    def _analyze_param_list(self, filename, elm, result):
        params = []
        for child in list(elm):
            if child.tag == "bullet_list":
                params = self._analyze_bullet_list(filename, child)
            elif child.tag == "paragraph":
                ls = child.find("literal_strong")
                if ls:
                    params = [ls.text]
                ls = child.find("strong")
                if ls:
                    params = [ls.text]
                else:
                    output_log(
                        LOG_LEVEL_WARN,
                        "<literal_strong> or <strong> is not found. "\
                        "(filename={0})".format(filename)
                    )

        if (result["type"] == "class") and ("params" not in result):
            return

        for p in params:
            if p not in result["params"]:
                output_log(
                    LOG_LEVEL_NOTICE,
                    "parameter '{0}' does not found ({1})".format(
                        p, result["name"])
                )

    def _analyze_field(self, filename, elm, result):
        field_type = ""
        for child in list(elm):
            if child.tag == "field_name":
                field_type = child.text
            elif child.tag == "field_body":
                if field_type == "Parameters":
                    self._analyze_param_list(filename, child, result)
                elif field_type == "Return type":
                    result["return_type"] = self._analyze_paragraph(filename,
                                                                    child)
                elif field_type == "Returns":
                    result["return_desc"] = self._analyze_paragraph(filename,
                                                                    child)

    def _analyze_field_list(self, filename, elm, result):
        for child in list(elm):
            if child.tag == "field":
                self._analyze_field(filename, child, result)

    def _analyze_desc_content(self, filename, elm, result):
        for child in list(elm):
            if child.tag == "paragraph":
                result["desc"] = self._analyze_paragraph(filename, child)
            elif child.tag == "field_list":
                self._analyze_field_list(filename, child, result)
            elif child.tag == "desc":
                self._analyze_desc(filename, child, result)

    def _analyze_desc_parameter(self, filename, elm, result):
        return elm.text

    def _analyze_desc_parameterlist(self, filename, elm, result):
        result["params"] = []
        for child in list(elm):
            if child.tag == "desc_parameter":
                param = self._analyze_desc_parameter(filename, child, result)
                result["params"].append(param)

    def _analyze_function(self, filename, elm, result):
        result["type"] = "function"
        for child in list(elm):
            if child.tag == "desc_signature":
                fullname = child.get("fullname")
                text = child.find("desc_name").text
                lp = text.find("(")
                rp = text.find(")")

                if lp == -1:
                    output_log(
                        LOG_LEVEL_NOTICE,
                        "'(' and ')' are not found (text={0})".format(text)
                    )
                    result["name"] = text
                    c = child.find("desc_parameterlist")
                    if c is not None:
                        self._analyze_desc_parameterlist(filename, c, result)
                    else:
                        result["params"] = []
                else:
                    result["name"] = text[0:lp]
                    result["params"] = [
                        re.sub(" ", "", p) for p in text[lp + 1:rp].split(",")
                    ]
                if result["name"] != fullname:
                    if fullname is not None:
                        output_log(
                            LOG_LEVEL_NOTICE,
                            "fullname does not match text (fullname={0}, \
                            text={1})".format(fullname, result["name"])
                        )
                result["module"] = child.get("module")
                result["class"] = child.get("class")
            elif child.tag == "desc_content":
                self._analyze_desc_content(filename, child, result)

    def _analyze_class(self, filename, elm, result):
        result["type"] = "class"
        result["method"] = []
        result["attribute"] = []
        for child in list(elm):
            if child.tag == "desc_signature":
                result["name"] = child.get("fullname")
                result["module"] = child.get("module")
            elif child.tag == "desc_content":
                self._analyze_desc_content(filename, child, result)

    def _analyze_attribute(self, filename, elm):
        attr = {"type": "attribute"}
        for child in list(elm):
            if child.tag == "desc_signature":
                attr["name"] = child.get("fullname")
                attr["module"] = child.get("module")
                attr["class"] = child.get("class")
                idx = attr["name"].rfind(attr["class"])
                if idx != -1:
                    attr["name"] = attr["name"][idx+len(attr["class"])+1:]
            elif child.tag == "desc_content":
                self._analyze_desc_content(filename, child, attr)

        return attr

    def _analyze_method(self, filename, elm):
        method = {"type": "method"}
        for child in list(elm):
            if child.tag == "desc_signature":
                if "name" in method:
                    continue
                fullname = child.get("fullname")
                text = child.find("desc_name").text
                lp = text.find("(")
                rp = text.find(")")
                if lp == -1:
                    output_log(
                        LOG_LEVEL_NOTICE,
                        "'(' and ')' are not found (text=" + text + ")"
                    )
                    method["name"] = text
                    c = child.find("desc_parameterlist")
                    if c is not None:
                        self._analyze_desc_parameterlist(filename, c, method)
                    else:
                        method["params"] = []
                else:
                    method["name"] = text[0:lp]
                    method["params"] = [
                        re.sub(" ", "", p) for p in text[lp + 1:rp].split(",")
                    ]
                if method["name"] != fullname:
                    if fullname is not None:
                       output_log(
                           LOG_LEVEL_NOTICE,
                           "fullname does not match text (fullname={0}, \
                           text={1})".format(fullname, method["name"])
                       )
                try:
                    method["params"].remove("self")
                except ValueError:
                    pass
                method["module"] = child.get("module")
                method["class"] = child.get("class")
            elif child.tag == "desc_content":
                self._analyze_desc_content(filename, child, method)

        return method

    def _analyze_data(self, filename, elm, result):
        result["type"] = "data"
        for child in list(elm):
            if child.tag == "desc_signature":
                result["name"] = child.get("fullname")
                if result["name"] is None:
                    result["name"] = child.find("desc_name").text
                result["module"] = child.get("module")
            elif child.tag == "desc_content":
                self._analyze_desc_content(filename, child, result)

    def _analyze_desc(self, filename, desc, result):
        attr = desc.get("desctype")
        if attr == "function":
            if ("type" in result) and (result["type"] == "class"):
                m = self._analyze_method(filename, desc)
                if "method" not in result:
                    result["method"] = []
                result["method"].append(m)
            else:
                self._analyze_function(filename, desc, result)
        elif attr == "class":
            self._analyze_class(filename, desc, result)
        elif attr == "attribute":
            a = self._analyze_attribute(filename, desc)
            if "attribute" not in result:
                result["attribute"] = []
            result["attribute"].append(a)
        elif attr == "method":
            if ("type" in result) and (result["type"] == "class"):
                m = self._analyze_method(filename, desc)
                if "method" not in result:
                    result["method"] = []
                result["method"].append(m)
            else:
                self._analyze_function(filename, desc, result)
        elif attr == "data":
            self._analyze_data(filename, desc, result)

    def _analyze_section(self, filename, elm, result):
        for child in list(elm):
            r = {}
            if child.tag == "desc":     # <desc>
                self._analyze_desc(filename, child, r)
                result.append(r)
            elif child.tag == "section":    # <section>
                self._analyze_section(filename, child, result)

    def _modify(self, result):
        pass

    def analyze(self, filename):
        tree = et.parse(filename)
        root = tree.getroot()       # <document>
        result = []
        for child in list(root):
            if child.tag == "section":    # <section>
                r = []
                self._analyze_section(filename, child, r)
                result.append(r)

        self._modify(result)

        return result


class MathutilsAnalyzer(BaseAnalyzer):
    def _modify(self, result):
        for sections in result:
            sections.insert(0, {"type": "data", "name": "STDPERLIN"})
            for s in sections:
                if s["type"] == "function":
                    for i, p in enumerate(s["params"]):
                        s["params"][i] = re.sub("=noise.types.", "=", p)
                    if s["name"] == "barycentric_transform":
                        s["params"][4] = "tri_b1"
                        s["params"][5] = "tri_b2"
                        s["params"][6] = "tri_b3"
                    elif s["name"] == "intersect_point_line":
                        s["params"][2] = "line_p2"
                elif s["type"] == "class":
                    # add __init__ method if __init__ is missing.
                    # all classes defined in mathutils module don't have
                    # __init__ method
                    found = False
                    for m in s["method"]:
                        if m["name"] == "__init__":
                            found = True
                            break
                    if not found:
                        if s["name"] == "KDTree":
                            s["method"].append({
                                "name": "__init__",
                                "params": ["size"],
                            })
                        elif s["name"] != "BVHTree":
                            s["method"].append({
                                "name": "__init__",
                                "params": ["val"],
                            })


class BpyExtraAnalyzer(BaseAnalyzer):
    def _modify(self, result):
        for sections in result:
            for s in sections:
                if s["type"] == "function":
                    if s["name"] == "path_reference_copy":
                        s["params"][1] = "report='print'"


class BmeshAnalyzer(BaseAnalyzer):
    def __rename_duplicate(self, lists):
        for l in lists:
            count = 0
            for i, s in enumerate(lists):
                if l == s:
                    count = count + 1
                    if count >= 2:
                        lists[i] = s + "_" + str(count)

    def _modify(self, result):
        for sections in result:
            for s in sections:
                if s["type"] == "function":
                    if s["name"] == "wireframe":
                        self.__rename_duplicate(s["params"])


class GpuAnalyzer(BaseAnalyzer):
    def _modify(self, result):
        for sections in result:
            for s in sections:
                if s["type"] == "data":
                    if s["name"] == "GPU_DYNAMIC_MIST_ENABLE:":
                        s["name"] = s["name"][:-1]


class FreestyleAnalyzer(BaseAnalyzer):
    def _modify(self, result):
        for sections in result:
            for s in sections:
                if s["type"] == "class":
                    if s["name"] == "SmoothingShader":
                        for m in s["method"]:
                            if m["name"][0:9] == "__init__":
                                m["name"] = "__init__"
                                m["params"] = [
                                    "num_iterations=100",
                                    "factor_point=0.1",
                                    "factor_curvature=0.0",
                                    "factor_curvature_difference=0.2",
                                    "aniso_point=0.0",
                                    "aniso_normal=0.0",
                                    "aniso_curvature=0.0",
                                    "carricature_factor=1.0"
                                ]
                elif s["type"] == "function":
                    if (s["name"] == "angle_x_normal") or \
                       (s["name"] == "normal_at_I0D"):
                        for i, p in enumerate(s["params"]):
                            if p == "it: Interface0DIterator":
                                s["params"][i] = p[0:2]
                    elif s["name"] == "pairwise":
                        s["params"].pop()
                        for i, p in enumerate(s["params"]):
                            if p[0:6] == "types=":
                                s["params"][i] = "types={}"


class BaseGenerator:
    def _write_function(self, file, data):
        file.write("def " + data["name"] + "(")
        if len(data["params"]):
            file.write(", ".join(data["params"]))
        file.write("):\n")
        file.write(INDENT + "pass" + "\n")
        file.write("\n\n")

    def _write_class(self, file, data):
        no_entry = True
        if data["name"] is None:
            output_log(
                LOG_LEVEL_WARN,
                "Failed to write class. (filename={0})"\
                .format(file)
            )
            return
        file.write("class " + data["name"] + ":\n")
        if "attribute" in data:
            for a in data["attribute"]:
                file.write(INDENT + a["name"] + " = None\n")
                no_entry = False
            file.write("\n")
        if "method" in data:
            for m in data["method"]:
                file.write(INDENT + "def " + m["name"] + "(self")
                if len(m["params"]):
                    file.write(", " + ", ".join(m["params"]))
                file.write("):\n")
                file.write(INDENT * 2 + "pass\n")
                file.write("\n")
                no_entry = False
        if no_entry:
            file.write(INDENT + "pass\n")
        file.write("\n\n")

    def _write_data(self, file, data):
        file.write(data["name"] + " = None\n")
        file.write("\n\n")

    def generate(self, filename, data):
        with open(filename, "w") as file:
            for sections in data:
                for s in sections:
                    if "type" not in s:
                        continue
                    if s["type"] == "function":
                        self._write_function(file, s)
                    elif s["type"] == "class":
                        self._write_class(file, s)
                    elif s["type"] == "data":
                        self._write_data(file, s)


# build module structure
def build_mod_structure(xml_files):
    def build(mod_name, mods):
        sp = mod_name.split(".")
        for m in mods:
            if m["name"] == sp[0]:
                mod = m
                break
        else:
            mod = {"name": sp[0], "children": []}
            mods.append(mod)
        if len(sp) >= 2:
            s = ".".join(sp[1:])
            build(s, mod["children"])

    raw = []
    for f in xml_files:
        idx = f.rfind("/")
        raw.append(f[idx+1:-4])        # strip .xml
    modules = []
    for r in raw:
        build(r, modules)

    return modules


def make_mod_dirs(base_path, tables):
    for t in tables:
        mod_name = base_path + "/" + t["mod"]
        idx = mod_name.rfind("/")
        dir_name = mod_name[:idx]
        pathlib.Path(dir_name).mkdir(parents=True, exist_ok=True)
        if dir_name == base_path:
            continue
        with open(dir_name + "/__init__.py", "w"):
            pass


def find_mod(modules, xml_file):
    idx = xml_file.rfind("/")
    modname_raw = xml_file[idx+1:-4]        # strip .xml
    modname_raw = re.sub("\.", "/", modname_raw)

    def find(name, mods, raw):
        for m in mods:
            mod_name = name + m["name"]
            if mod_name == raw:
                if len(m["children"]) == 0:
                    return mod_name + ".py"
                else:
                    return mod_name + "/__init__.py"
            if len(m["children"]) > 0:
                ret = find(mod_name + "/", m["children"], raw)
                if ret:
                    return ret

    return find("", modules, modname_raw)


def build_mod_xml_table(mods, xml_files):
    tables = []

    for f in xml_files:
        item = {"xml": f, "mod": find_mod(mods, f)}
        tables.append(item)

    return tables


def gen_package(path, xml_files, analyzer, generator):
    # build module structure
    mods = build_mod_structure(xml_files)

    # build module-xml table
    tables = build_mod_xml_table(mods, xml_files)

    # create directory
    make_mod_dirs(path, tables)

    # create modules
    for t in tables:
        r = analyzer.analyze(t["xml"])
        generator.generate(path + "/" + t["mod"], r)


def gen_bpy_package():
    all_files = glob.glob(INPUT_DIR + "/bpy*.xml")
    excludes_files = glob.glob(INPUT_DIR + "/bpy_extras*.xml")
    files = list(set(all_files) - set(excludes_files))
    gen_package(OUTPUT_DIR, files, BaseAnalyzer(), BaseGenerator())


def gen_bgl_module():
    files = glob.glob(INPUT_DIR + "/bgl*.xml")
    gen_package(OUTPUT_DIR, files, BaseAnalyzer(), BaseGenerator())


def gen_blf_module():
    files = glob.glob(INPUT_DIR + "/blf*.xml")
    gen_package(OUTPUT_DIR, files, BaseAnalyzer(), BaseGenerator())


def gen_mathutils_package():
    files = glob.glob(INPUT_DIR + "/mathutils*.xml")
    gen_package(OUTPUT_DIR, files, MathutilsAnalyzer(), BaseGenerator())


def gen_gpu_module():
    files = glob.glob(INPUT_DIR + "/gpu*.xml")
    gen_package(OUTPUT_DIR, files, GpuAnalyzer(), BaseGenerator())


def gen_freestyle_package():
    files = glob.glob(INPUT_DIR + "/freestyle*.xml")
    gen_package(OUTPUT_DIR, files, FreestyleAnalyzer(), BaseGenerator())


def gen_bpy_extra_package():
    files = glob.glob(INPUT_DIR + "/bpy_extras*.xml")
    gen_package(OUTPUT_DIR, files, BpyExtraAnalyzer(), BaseGenerator())


def gen_aud_module():
    files = glob.glob(INPUT_DIR + "/aud*.xml")
    gen_package(OUTPUT_DIR, files, BaseAnalyzer(), BaseGenerator())


def gen_bmesh_package():
    files = glob.glob(INPUT_DIR + "/bmesh*.xml")
    gen_package(OUTPUT_DIR, files, BmeshAnalyzer(), BaseGenerator())


def parse_options():
    global INPUT_DIR, OUTPUT_DIR
    usage = "Usage: python {} [-i <input_dir>] [-o <output_dir>]"\
        .format(__file__)
    parser = argparse.ArgumentParser(usage)
    parser.add_argument(
        "-i", dest="input_dir", type=str, help="Input Directory"
    )
    parser.add_argument(
        "-o", dest="output_dir", type=str, help="Output Directory"
    )
    args = parser.parse_args()
    if args.input_dir:
        INPUT_DIR = args.input_dir
    if args.output_dir:
        OUTPUT_DIR = args.output_dir


def main():
    parse_options()
    gen_bpy_package()
    gen_bgl_module()
    gen_blf_module()
    gen_mathutils_package()
    gen_gpu_module()
    gen_freestyle_package()
    gen_bpy_extra_package()
    gen_aud_module()
    gen_bmesh_package()


if __name__ == "__main__":
    main()

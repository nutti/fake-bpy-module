FROM docker:24-cli

# Make local cache directory for volume
RUN mkdir /act_cache \
 && chmod -R 1777 /act_cache

# Make actions/cache directory for volume
RUN mkdir /act_cache_server \
 && chmod -R 1777 /act_cache_server

# Make artifact directory
RUN mkdir /act_artifacts \
 && chmod -R 1777 /act_artifacts

# Install dependencies
RUN apk add --no-cache bash curl

# Install act
ENV ACT_VERSION=0.2.56
RUN curl https://raw.githubusercontent.com/nektos/act/master/install.sh | bash
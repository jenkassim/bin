# Heroku

# Installation CLI
- Install standalone version since not supported by dnf
```
    $ wget https://cli-assets.heroku.com/heroku-cli/channels/stable/heroku-cli-linux-x86.tar.gz -O heroku.tar.gz
    $ tar -xvzf heroku.tar.gz
    $ mkdir -p /usr/local/lib /usr/local/bin
    $ mv heroku-cli-v6.x.x-darwin-64 /usr/local/lib/heroku
    $ ln -s /usr/local/lib/heroku/bin/heroku /usr/local/bin/heroku
```

- Add to env PATH in ~/.bash_profile
```
    export PATH=$PATH:/usr/local/bin/heroku
```

# Running Heroku-CLI
- Login : ` $ heroku login`

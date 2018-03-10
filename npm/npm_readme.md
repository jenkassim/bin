# Node.js -NPM
- Node Package Manager for node.js packages.

## Installation
- Npm installation : `$ sudo dnf install npm`
- Check version : `$ npm --version`
- Default modules installed locally (in specified folder) and accessible via `require()` method.
```
    - Local installation
    $ npm install <module>
    $ var obj = require('module')
    - Global installation
    $ npm install <module> -g
```

- Check installed modules
```
    - Local modules
    $ ls -l
    - Global modules
    4 ls -g
```

- Uninstall Module
```
    $ npm uninstall <module>
```

- Update module : `$ npm update <module>
- Search module : `$ npm search <module>

## JSON Package
- `package.json` present in root directory of any Mode app/module to define package properties.
# Installing
In order to install the front-end requirements, you must first install `Node.js` from (URL). Once this is done, all following packages can be installed using the `package.json` file. This can be done by running the following command at the front-end folder:

```
npm install
```

This command retrieves all package dependencies and installs them.


# Deploying
Once all dependencies are installed, the front-end survey can be instantiated via the `deploy.bat` file. It runs the basic shell command:

```shell
npm start
```
Once the front-end server is running, it can be accessed at the port `localhost:3000`. Accessing the web application requires using specific _magic links_ so that the application can identify the _view_ that it needs to serve.

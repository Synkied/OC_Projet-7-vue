var express = require('../frontend/node_modules/express');
var serveStatic = require('../frontend/node_modules/serve-static');

app = express();
app.use(serveStatic(__dirname));

var port = process.env.PORT || 5000;
app.listen(port);

console.log('server started '+ port);
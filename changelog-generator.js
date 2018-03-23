var fs = require('fs');
var execSync = require('child_process').exec;

var file = 'changelog.md';
var cmd = 'git log --no-merges --pretty=format:\"%D -[%h] %s\" >' + file;

execSync(cmd, 'utf8', function () {
  fs.readFile(file, 'utf8', function (err, data) {
    if (err) {
      return console.log(err);
    }
    var result = data.replace(/tag:(.*) -(.*)/g, '### $1').replace(/\n/g, '\r\n');
    fs.writeFile(file, result, 'utf8', function (err) {
      if (err) {
        return console.log(err);
      }
    });
  });
  return;
});


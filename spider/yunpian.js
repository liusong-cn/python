var r = function(){
   return Math.random().toString(32).replace("0.","")
}

var createUUID = function(){
    var n = (new Date).getTime();
    var perf = require('perf_hooks');

    var performance = perf.performance.now()
        return performance && "function" == typeof performance.now && (n += performance.now()),
        "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function(t) {
            var e = (n + 16 * Math.random()) % 16 | 0;
            return n = Math.floor(n / 16),
            ("x" === t ? e : 3 & e | 8).toString(16)
        })
}

var getRandomStr = function(t){
    for (var e = ""; e.length < t; )
            e += Math.random().toString(36).substr(2);
        return e = e.slice(0, t)
}

var  r = Object.create || function() {
        function n() {}
        return function(t) {
            var e;
            return n.prototype = t,
            e = new n,
            n.prototype = null,
            e
        }
    }();
var o;
var  a = (o = {}).lib = {};
var s = a.Base = {
        extend: function(t) {
            var e = r(this);
            return t && e.mixIn(t),
            e.hasOwnProperty("init") && this.init !== e.init || (e.init = function() {
                e.$super.init.apply(this, arguments)
            }
            ),
            (e.init.prototype = e).$super = this,
            e
        },
        create: function() {
            var t = this.extend();
            return t.init.apply(t, arguments),
            t
        },
        init: function() {},
        mixIn: function(t) {
            for (var e in t)
                t.hasOwnProperty(e) && (this[e] = t[e]);
            t.hasOwnProperty("toString") && (this.toString = t.toString)
        },
        clone: function() {
            return this.init.prototype.extend(this)
        }
    };
var  d = a.WordArray = s.extend({
        init: function(t, e) {
            t = this.words = t || [],
            this.sigBytes = null != e ? e : 4 * t.length
        },
        toString: function(t) {
            return (t || l).stringify(this)
        },
        concat: function(t) {
            var e = this.words
              , n = t.words
              , i = this.sigBytes
              , r = t.sigBytes;
            if (this.clamp(),
            i % 4)
                for (var o = 0; o < r; o++) {
                    var a = n[o >>> 2] >>> 24 - o % 4 * 8 & 255;
                    e[i + o >>> 2] |= a << 24 - (i + o) % 4 * 8
                }
            else
                for (var o = 0; o < r; o += 4)
                    e[i + o >>> 2] = n[o >>> 2];
            return this.sigBytes += r,
            this
        },
        clamp: function() {
            var t = this.words
              , e = this.sigBytes;
            t[e >>> 2] &= 4294967295 << 32 - e % 4 * 8,
            t.length = h.ceil(e / 4)
        },
        clone: function() {
            var t = s.clone.call(this);
            return t.words = this.words.slice(0),
            t
        },
        random: function(t) {
            for (var e, n = [], i = function(e) {
                var e = e
                  , n = 987654321
                  , i = 4294967295;
                return function() {
                    var t = ((n = 36969 * (65535 & n) + (n >> 16) & i) << 16) + (e = 18e3 * (65535 & e) + (e >> 16) & i) & i;
                    return t /= 4294967296,
                    (t += .5) * (.5 < h.random() ? 1 : -1)
                }
            }, r = 0; r < t; r += 4) {
                var o = i(4294967296 * (e || h.random()));
                e = 987654071 * o(),
                n.push(4294967296 * o() | 0)
            }
            return new d.init(n,t)
        }
    });
var  c = o.enc = {};
var u = c.Latin1 = {
        stringify: function(t) {
            for (var e = t.words, n = t.sigBytes, i = [], r = 0; r < n; r++) {
                var o = e[r >>> 2] >>> 24 - r % 4 * 8 & 255;
                i.push(String.fromCharCode(o))
            }
            return i.join("")
        },
        parse: function(t) {
            for (var e = t.length, n = [], i = 0; i < e; i++)
                n[i >>> 2] |= (255 & t.charCodeAt(i)) << 24 - i % 4 * 8;
            return new d.init(n,e)
        }
    };
var w = r.format = {};

var T = w.OpenSSL = {
        stringify: function(t) {
            var e = t.ciphertext
              , n = t.salt;
            if (n)
                var i = c.create([1398893684, 1701076831]).concat(n).concat(e);
            else
                var i = e;
            return i.toString(u)
        },
        parse: function(t) {
            var e = u.parse(t)
              , n = e.words;
            if (1398893684 == n[0] && 1701076831 == n[1]) {
                var i = c.create(n.slice(2, 4));
                n.splice(0, 4),
                e.sigBytes -= 16
            }
            return b.create({
                ciphertext: e,
                salt: i
            })
        }
    };

var  A = o.SerializableCipher = a.extend({
        cfg: a.extend({
            format: T
        }),
        encrypt: function(t, e, n, i) {
            i = this.cfg.extend(i);
            var r = t.createEncryptor(n, i)
              , o = r.finalize(e)
              , a = r.cfg;
            return b.create({
                ciphertext: o,
                key: n,
                iv: a.iv,
                algorithm: t,
                mode: a.mode,
                padding: a.padding,
                blockSize: t.blockSize,
                formatter: i.format
            })
        },
        decrypt: function(t, e, n, i) {
            i = this.cfg.extend(i),
            e = this._parse(e, i.format);
            var r = t.createDecryptor(n, i).finalize(e.ciphertext);
            return r
        },
        _parse: function(t, e) {
            return "string" == typeof t ? e.parse(t, this) : t
        }
    });
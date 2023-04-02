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

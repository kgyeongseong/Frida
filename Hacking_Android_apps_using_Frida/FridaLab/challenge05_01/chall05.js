setImmediate(function() {
    Java.perform(function() {
        var chall_05 = Java.use("uk.rossmarks.fridalab.MainActivity");
        chall_05.chall05.overload("java.lang.String").implementation = function(arg) {
            this.chall05("frida");
            console.log("\nSolved Challenge 05");
        }
    })
})
setImmediate(function() {
    Java.perform(function() {
        var chall_03 = Java.use("uk.rossmarks.fridalab.MainActivity");
        chall_03.chall03.implementation = function() {
            console.log("\nSolved Challenge 03");
            return true;
        }
    })
})
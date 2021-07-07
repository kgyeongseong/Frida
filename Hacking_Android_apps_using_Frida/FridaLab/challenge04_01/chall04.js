setImmediate(function() {
    Java.perform(function() {
        Java.choose("uk.rossmarks.fridalab.MainActivity", {
            "onMatch": function(chall_04) {
                chall_04.chall04("frida");
            },
            "onComplete": function() {
                console.log("\nSolved Challenge 04");
            }
        })
    })
})
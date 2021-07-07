setImmediate(function() {
    Java.perform(function() {
        Java.choose("uk.rossmarks.fridalab.MainActivity", {
            "onMatch": function(chall_02) {
                chall_02.chall02();
            },
            "onComplete": function() {
                console.log("\nSolved Challenge 02");
            }
        })
    })
})
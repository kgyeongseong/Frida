import frida, sys

jscode = """
Java.perform(function() {
    
    //chall01
    var challenge_01 = Java.use('uk.rossmarks.fridalab.challenge_01');

    challenge_01.chall01.value = 1;

    //chall02
    var main;
    Java.choose('uk.rossmarks.fridalab.MainActivity', {
        onMatch: function(instance) {
            main = instance;
        },
        onComplete: function() {}
    });

    main.chall02();

    //chall03
    var main;
    Java.choose('uk.rossmarks.fridalab.MainActivity', {
        onMatch: function(instance) {
            main = instance;
        },
        onComplete: function() {}
    });

    main.chall03.implementation = function() {
        return true;
    }

    //chall04
    var main;
    Java.choose('uk.rossmarks.fridalab.MainActivity', {
        onMatch: function(instance) {
            main = instance;
        },
        onComplete: function() {}
    });

    main.chall04('frida');

    var count = 0;

    //chall05
    var chall_05 = Java.use('uk.rossmarks.fridalab.MainActivity');
    chall_05.chall05.overload('java.lang.String').implementation = function(arg0) {
        if (count < 5)
        {
            count++;
            this.chall05('frida');
        }
        return;
    }

    //chall06
    var main;
    Java.choose('uk.rossmarks.fridalab.MainActivity', {
        onMatch: function(instance) {
            main = instance;
        },
        onComplete: function() {}
    });

    var count = 0;

    main.chall06.overload('int').implementation = function(arg1) {
        if (count < 5)
        {
            count++;
            var chall_06 = Java.use('uk.rossmarks.fridalab.challenge_06');
            console.log(chall_06.chall06.value);
            this.chall06(chall_06.chall06.value);
        }
        return;
    }

    setTimeout(function(){
        main.chall06(1);
        console.log('challenge6 done.');
    }, 11000);
    
    //chall07
    var main;
    Java.choose('uk.rossmarks.fridalab.MainActivity', {
        onMatch: function(instance) {
            main = instance;
        },
        onComplete: function() {}
    });

    var challenge_07 = Java.use('uk.rossmarks.fridalab.challenge_07');
    
    var i;
    for (i = 0; i < 10000; i++)
    {
        if (challenge_07.check07Pin(i.toString()))
        {
            main.chall07(i.toString());
            break;
        }
            
    }

    //chall08
    var klass = Java.use('android.widget.Button');
    Java.choose('uk.rossmarks.fridalab.MainActivity', {
        onMatch : function(instance) {
            var checkid = instance.findViewById(2131165231);
            var check = Java.cast(checkid, klass);
            var string = Java.use('java.lang.String');
            check.setText(string.$new('Confirm'));
        },
        onComplete : function() {
        }
    });
});
"""

session = frida.get_usb_device(1).attach("uk.rossmarks.fridalab") # 크롬 앱 프로세스에 연결
script = session.create_script(jscode) # 삽입할 자바스크립트 코드 생성
script.load() # 생성한 스크립트 로드
sys.stdin.read() # 스크립트 삽입 전 종료되는 문제 방지
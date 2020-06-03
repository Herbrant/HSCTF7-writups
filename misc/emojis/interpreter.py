vardata = {
9800: 0,
9801: 0,
9802: 0,
9803: 0,
9804: 0,
9805: 0,
9806: 0,
9807: 0,
9808: 0,
9809: 0,
9810: 0,
9811: 0,
128336: 0,
128337: 0,
128338: 0,
128339: 0,
128340: 0,
128341: 0,
128342: 0,
128343: 0,
128344: 0,
128345: 0,
128346: 0,
128347: 0,
128680: 0, #command counter
128148: 0, #constant
128156: 1, #constant
128149: 2, #constant
128158: 4, #constant
128150: 8, #constant
127908: 0, #I/O
128226: 0, #I/O
}

constant=(128148,128156,128149,128158,128150)

class EmojiError(Exception): pass

def clean(setcmd=False):
    try:
        error=1
        assert cmd1 in vardata
        assert cmd2 in vardata
        error=2
        assert cmd1 not in constant
        if setcmd==False:
            error=4
            assert cmd1 != 128226
            assert cmd2 != 127908
        elif setcmd==True:
            error=3
            assert cmd1 != 127908
            assert cmd2 != 128226
            error=5
            assert not (cmd1 == 128226 and cmd2 == 127908)
    except AssertionError:
        errorlist={1:"🚫 🔡 ➡️ 🔲 🔳 ", 2:"🚫 💔 💜 💕 💞 💖 ➡️ 🔳 ", 3:"⚠ 🎤 ↔️ 📢",4:"🚫 🎤 📢 ➡️ 😇 😈 😵",5:"🚫 😊 📢 🎤",}
        print("💻  ⚠️ ➡️ 🚨  "+str(vardata[128680]))
        print(errorlist[error])
        print(print(chr(cmd0)+" "+chr(cmd1)+" "+chr(+cmd2)))
        raise EmojiError

import linecache
import sys
if len(sys.argv) == 1:
    print("Need filename")
    exit(1)
code = sys.argv[1] # this is filename, not the actual code

while 1 == 1:
    try:
        vardata[128680] = vardata[128680] + 1
        try:
            tempcmd = linecache.getline(code, vardata[128680])
        except EOFError:
            break
        if tempcmd == "":
            break
        if len(tempcmd) >= 3:
            cmd = tempcmd[0:3]
        else:
            cmd = "XXX"
        cmd0 = ord(cmd[0])
        cmd1 = ord(cmd[1])
        cmd2 = ord(cmd[2])
        if cmd0 == 128522:
            clean(True)
            if cmd1 == 128226:
                print(chr(vardata[cmd2]),end="",flush=True)
            elif cmd2 == 127908:
                vardata[cmd1]=input("\n🎤 > ")
                if vardata[cmd1]=="":
                    vardata[cmd1]=0
                else:
                    vardata[cmd1]=ord(vardata[cmd1][0])
            else:
                vardata[cmd1] = vardata[cmd2]
        elif cmd0 == 128519:
            clean()
            vardata[cmd1] = vardata[cmd1]+vardata[cmd2]
        elif cmd0 == 128520:
            clean()
            vardata[cmd1] = vardata[cmd1]-vardata[cmd2]
        elif cmd0 == 128565:
            clean()
            if vardata[cmd1] == vardata[cmd2]:
                vardata[128680] = vardata[128680] + 1
    except EmojiError:
        break

linecache.clearcache()
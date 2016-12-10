def char_convert(ch):
    if ch == "y":
        return "a"
    elif ch == "z":
        return "b"
    else:
        return chr (ord(ch)+2)

message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb " \
          "rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
''.join(list(map(char_convert, message)))



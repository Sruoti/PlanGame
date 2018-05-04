try:
   with open('C:\\Users\\ZHJ\\Desktop\\test.txt',decoding='gbk',mode='r') as f:
        f.read()
        f.close()
except UnicodeDecodeError as reason:
    print('unicode error:',reason)
except OSError:
    print('os error')
except (TabError, TypeError) as reason:  #多个异常放在一起
    print('多个error', reason)
finally:
    print('MMP')
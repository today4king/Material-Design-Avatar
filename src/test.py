from src.avatars import  avatars

j=avatars('123@123.com','Frederick')
j.avatar_gen_img()
j.save("../examples")
k=avatars('king@123.com','George ')
k.avatar_gen_img()
k.save("../examples")
w=avatars('王林')
w.avatar_gen_img()
w.save("../examples")
# avatar_gen_img('tom')
# avatar_gen_img('#￥%……')
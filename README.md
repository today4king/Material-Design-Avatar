# Material-Design-Avatar
Default avatar picture generate for python

# How it work
Hash an string can be guid or email to choose an backgroud color.
Generate a letter from the name or email.

# Examples
![avater](./examples/F_167_255_235.png)
![avater](./examples/G_255_152_0.png)
![avater](./examples/王_255_61_0.png)

#How to use
a = avatars(user.email, name=user.name)
filename = a.avatar_filename()
if not os.path.isfile(os.path.join(upload_dir, filename)):
    a.save(upload_dir)

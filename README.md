#…or create a new repository on the command line
...
 
 echo "# 1804w" >> README.md
 git init
 git add README.md
 git commit -m "first commit"
 git remote add origin https://github.com/wangxuewen123/1804w.git
 git push -u origin master
...
#…or push an existing repository from the command line
...

 
 git remote add origin https://github.com/wangxuewen123/1804w.git
 git push -u origin master


...
#以后要上传命令 就用这几个
...
git add .
git commit -m '上传的文件的说明'
git push -u origin master
...

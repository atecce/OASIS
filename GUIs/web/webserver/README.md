# WebServer README

Read the docs to get set up. Basically you'll have to run *npm install* from
this directory and then *gulp build* to convert the jade/less into html/css.


The dist directory is in the *.gitignore* file so you'll have to run *gulp build*
after you pull from the repo if you wish to see the latest changes on the webserver.


The first step is to remove the cluster of pages provided for us and add a bunch
of blank pages that we think we'll need. We can start by organizing our frontend's
skeleton.

# Things that might be helpful to have

Jade and Less syntax highlighting isn't included in vim by default. However, there are
plugins and plugin managers that make this easy.


This would be helpful because in order to make any changes to the webserver you must
edit the jade files. 


I recommend using vundle, here's a short tutorial to get it set up:


https://www.digitalocean.com/community/tutorials/how-to-use-vundle-to-manage-vim-plugins-on-a-linux-vps


And here's the repository you will want to add to vundle:


https://github.com/digitaltoad/vim-pug


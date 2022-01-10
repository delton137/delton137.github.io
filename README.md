Dan's webpage source
=====================================

Originally my blog and website were hosted on Wordpress. In 2017 I exported all of my wordpress content to [Jekyll](https://jekyllrb.com/) with hosting through GitHub pages.

I am grateful to [Steven Miller](https://github.com/svmiller) for creating the theme this is based off. [Check out his page](https://github.com/svmiller/steve-ngvb-jekyll-template) to use it yourself and find more documentation.

# Notes on how to build
To install the necessary gems:
`sudo bundle install`

If bundle can't find an old version of ruby, check the first line in the /usr/local/bin/bundle script to make sure it points to the ruby executable. 

To update Ruby gems and the bundler, as is needed periodically:

`bundle update --bundler`

`sudo gem update --system`

Once Jekyll and all the necessary Ruby "gems" are installed, the command to build the website is:

`jekyll serve`

to build while watching for changes:

`jekyll serve --watch`

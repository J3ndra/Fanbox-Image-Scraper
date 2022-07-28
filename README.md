# Fanbox Image Scraper

Tired downloading? try using this dumb code.

### Setup environment

- virtualenv <env_name> [**Create virtual environment**]
- source <env_name>/bin/activate [**Start**] || <env_name>\Scripts\activate.bat [**For Windows**]
- pip install -r req.txt [**Install packages needed**]
- deactivate [**Stop**]

### How to use it?

1. Login to Fanbox
2. Go to someone post
3. Inspect element there and go to network, filter to **Fetch/XHR**
4. And then copy `post.info` as cUrl (cmd)
   ![cUrl](https://raw.githubusercontent.com/J3ndra/Fanbox-Scraper-Python/main/docs/1.png)
5. Copy those curl in [this website](https://sqqihao.github.io/trillworks.html)
6. Copy `.env.example` to `.env`
7. Set 'cookie' in you `.env`
   ![cookie](https://raw.githubusercontent.com/J3ndra/Fanbox-Scraper-Python/main/docs/2.png)
8. Now you're ready to go!

### Example
![example 1](https://raw.githubusercontent.com/J3ndra/Fanbox-Scraper-Python/main/docs/example%20-%201.png)
class Codec:
    
    urls = []

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.urls.append(longUrl)
        return 'http://tinyurl.com/' + str(len(self.urls) - 1)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.urls[int(shortUrl.split('/')[-1])]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
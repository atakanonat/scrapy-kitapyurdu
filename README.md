
# Scrapy Kitapyurdu.com
A Scrapy project that takes all weekly best seller books from kitapyurdu.com.




## Requirements

python == 3.8.11\
scrapy == 2.4.1

  
## Usage

To put 'weeklybestsellers' spider to work, go to the project’s top level directory and run:

```bash
  scrapy crawl weeklybestsellers -o weeklybestsellers.jl
```
After a couple of seconds, you should see a JSON Lines file named weeklybestsellers.jl in project directory.
If you want the data as JSON format you can just change "weeklybestsellers.jl" to "weeklybestsellers.json".
But that may be cause some problem when you run spider twice.

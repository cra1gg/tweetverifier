# Python Tweet Verifier

Python script to verify whether or not specified image of a tweet is real or not. If it is, provides a link to said tweet as well as a similarity score/certainty percentage

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

Download Tesseract OCR from [here](https://github.com/UB-Mannheim/tesseract/wiki). Tessaract OCR requires Build Tools for C++ which can be downloaded from [here](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16)

OpenCV is also required which can be downloaded from [here](https://opencv.org/releases/)

```
pip install pytesseract
pip install pillow
```

### Installing

To run the program, clone the repo, and add it to the same directory as the photo of the tweet (png or jpeg)

Run the program using 

```
python main.py -i {Image Directory and Name} 
```

Example:

```
python main.py -i testtweets/test1.png
```

The program will return a list of matched tweets from most similar to least


## Built With

* [TesseractOCR](https://github.com/tesseract-ocr/)
* [numpy](https://numpy.org/)
* [GetOldTweets3](https://github.com/Mottl/GetOldTweets3)

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Craig D'Souza** - *Initial work* - [cra1gg](https://github.com/cra1gg)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Inspired by [NiroxGG's Reddit "RealTweetOrNot" bot](https://github.com/giulionf/realtweetornotbot)
* Thanks to [Mottl](https://github.com/Mottl/) for their amazing [Twitter API Python wrapper](https://github.com/Mottl/GetOldTweets3) 


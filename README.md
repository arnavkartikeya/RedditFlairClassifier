# RedditFlairClassifier
An nlp model (fasttext) which classifies what flair an r/AskScience post should have. Currently works with top 10 flairs, but in later iterations will work with all. Simply place the title or text of a reddit post from r/AskScience using the predict function and be returned a result including the appropriate flair and confidence. 

# Example: 

```
predict("Why are different wavelengths of light refracted by different amounts?")
console: (('__label__Physics',), array([0.80585706]))

predict("In a cosmic year (the sun orbiting the Milky Way once) about how much variation would the solar system experience from outside forces?")
console: (('__label__Astronomy',), array([0.90617985]))
```

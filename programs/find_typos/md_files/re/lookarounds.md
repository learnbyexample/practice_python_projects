# Lookarounds

In this chapter you'll learn more groupins, known as lookarounds, that  
help to create custom anchors and add conditions within RE definition.

## Negative lookarounds

* `(?!pat)` — negative lookahead assertion
* `(?<!pat)` — negative lookbehind assertion

```ruby
>>> re.sub(r'foo(?!\d)', 'baz', 'hey food! foo42 foot5 foofoo')
'hey bazd! foo42 bazt5 bazbaz'

>>> re.sub(r'(?<!_)foo', 'baz', 'foo _foo 42foofoo')
'baz _foo 42bazbaz'
```

## Positive lookarounds

* `(?=pat)` — positive lookahead assertion
* `(?<=pat)` — positive lookbehind assertion

```ruby
>>> re.findall(r'(?<=-)\d+(?=[:;])', '42 foo-5, baz3; x-83, y-20: f12')
['20']

>>> re.sub(r'par(?=.*\bpart\b)', 'X', 'par spare part party')
'X sXe part party'
```

# Selenium Examples

## Scroll Down

```
./scroll_down.py
```

## Get Google Map Coordinates

```
atom .phrases
LIST=`cat .phrases | while read -r line; do echo \"$line\"; done`; echo $LIST
./get_coordinates.py <paste>
```

or

```
atom .postcodes
LIST=`cat .postcodes | while read -r line; do echo \"$line\"; done`; echo $LIST
./get_coordinates.py <paste>
```

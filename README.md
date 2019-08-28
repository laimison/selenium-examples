# Selenium Examples

## Scroll Down

```
./scroll_down.py
```

## Get Google Map Coordinates

```
atom .phrases
LIST=`cat .phrases | while read -r line; do echo \"$line\"; done`
./get_coordinates.py $(cat .phrases)
```

or

```
atom .postcodes
./get_coordinates.py `cat .postcodes | while read -r line; do echo \'$line\'; done`
```

# Selenium Examples

## Scroll Down

```
./scroll_down.py
```

## Get Google Map Coordinates

```
atom .phrases
LIST=`cat .phrases | while read -r line; do echo \"$line\"; done`; echo $LIST
./get_coordinates.py <paste> | tee -a /var/tmp/coordinates-${RANDOM}.log
```

or

```
atom .postcodes
LIST=`cat .postcodes | while read -r line; do echo \"$line\"; done`; echo $LIST
./get_coordinates.py <paste> | tee -a /var/tmp/coordinates-${RANDOM}.log
```

PICS=$(wildcard pictures/*.jpg)
THUMBS=$(PICS:pictures/%.jpg=thumbs/%.jpg)
all: $(THUMBS)
thumbs/%.jpg: pictures/%.jpg
	convert -thumbnail 100 $^ $@

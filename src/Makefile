# REQUIRED TARGETS (all, pack, clean, test, doc, run, profile)
all: run profile

#pack: TODO zabalenie projektu na odovzdanie

doc: Doxyfile doc_clean
	mkdir ../doc && cd ../doc && doxygen ../src/$<

doc_clean:
	cd .. && rm -rf doc 

run: main.py
	python3 main.py

profile: stddev.py
	chmod +x stddev.py

test: 
	python3 -m MathLib_Tests

clean: # TODO - vymazanie suborov, ktore nemaju byt odovzdane

# Must be generated before installation
reqs:
	pip3 freeze > requirements.txt

init:
	pip3 install -r requirements.txt


generate-prof-input:
	../profiling/generate 
	mv data_*.txt ../profiling/data_input


.PHONY: all doc doc_clean run profile test clean reqs init generate-prof-input

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
	rm -f data_*.txt test.pstats* output_*.png requirements.txt

# Must be generated before installation
reqs:
	pip3 freeze > requirements.txt

init:
	pip3 install -r requirements.txt


profiling-input:
	../profiling/generate 
	mv data_*.txt ../profiling/profiling_input

profiler-output:
	python3 -m cProfile -o test.pstats10 \
		./stddev.py < ../profiling/profiling_input/data_10.txt
	python3 -m cProfile -o test.pstats100 \
		./stddev.py < ../profiling/profiling_input/data_100.txt
	python3 -m cProfile -o test.pstats1000 \
		./stddev.py < ../profiling/profiling_input/data_1000.txt
	mv test.pstats* ../profiling/profiler_output

profiling-images:
	gprof2dot -f pstats ../profiling/profiler_output/test.pstats10 | dot -Tpng -o output_10.png
	gprof2dot -f pstats ../profiling/profiler_output/test.pstats100 | dot -Tpng -o output_100.png
	gprof2dot -f pstats ../profiling/profiler_output/test.pstats1000 | dot -Tpng -o output_1000.png
	mv output_*.png ../profiling/


.PHONY: all reqs init profiling-input profiler-output profile test clean

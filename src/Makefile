profiling:
	./gen_input_files
	python3 -m cProfile -o test.pstats10 ./standardDeviation.py < data_10.txt
	python3 -m cProfile -o test.pstats100 ./standardDeviation.py < data_100.txt
	python3 -m cProfile -o test.pstats1000 ./standardDeviation.py < data_1000.txt
	gprof2dot -f pstats test.pstats10 | dot -Tpng -o output_10.png
	gprof2dot -f pstats test.pstats100 | dot -Tpng -o output_100.png
	gprof2dot -f pstats test.pstats100 | dot -Tpng -o output_1000.png

testing: 
	python3 -m MathLib_Tests

clean:
	rm -f data_*.txt test.pstats* output_*.png

profiling:
	./gen_input_files
	./standardDeviation.py < data_10.txt
	./standardDeviation.py < data_100.txt
	./standardDeviation.py < data_1000.txt

testing: 
	python3 -m MathLib_Tests

clean:
	rm -f data_*.txt

# Contains every file necessarry
MAIN_FOLDER := calculathor-1.0

all: run profile

pack: doc package
	cd ../.. && zip -r xhrabo15_xsmyka01_xsmida03_xbucko05.zip xhrabo15_xsmyka01_xsmida03_xbucko05

package: 
	mkdir -p ../../xhrabo15_xsmyka01_xsmida03_xbucko05/repo
	mkdir ../../xhrabo15_xsmyka01_xsmida03_xbucko05/install
	mkdir ../../xhrabo15_xsmyka01_xsmida03_xbucko05/doc
	cp -a ../../IVS_TeamProject/. ../../xhrabo15_xsmyka01_xsmida03_xbucko05/repo/
	cp -a ../doc/. ../../xhrabo15_xsmyka01_xsmida03_xbucko05/doc/
	cp -a ../install/. ../../xhrabo15_xsmyka01_xsmida03_xbucko05/install/

doc: Doxyfile
	cd .. && rm -rf doc 
	mkdir ../doc
	doxygen && rm -rf latex && mv html ../doc

run: main.py
	python3 main.py

profile: stddev.py
	chmod +x stddev.py

test: MathLib_Tests.py
	python3 -m MathLib_Tests

clean:
	rm -rf __pycache__
	rm -rf ../doc
	rm ../../xhrabo15_xsmyka01_xsmida03_xbucko05.zip

# Must be generated before installation
reqs:
	pip3 freeze > requirements.txt

generate-prof-input:
	../profiling/generate 
	mv data_*.txt ../profiling/data_input

deb:
	cd ../install/ && rm -f calculathor_1.0_amd64.deb
	cd ../../ && tar czvf $(MAIN_FOLDER).tar.gz $(MAIN_FOLDER)
	cd ../ && dpkg-buildpackage -rfakeroot -uc -b
	cd ../../ && mv calculathor_1.0_amd64.deb $(MAIN_FOLDER)/install/

.PHONY: all doc run profile test clean reqs init generate-prof-input

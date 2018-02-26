/*
 * Pixel.hpp
 *
 *  Created on: Feb 26, 2018
 *      Author: Derek
 */

#ifndef SRC_MODEL_PIXEL_HPP_
#define SRC_MODEL_PIXEL_HPP_

class Pixel {
public:
	Pixel();
	virtual ~Pixel();
	//Getters
	int returnRed();
	int returnGreen();
	int returnBlue();


	//Settings
	int setRed(int r);
	int setGreen(int g);
	int setBlue(int b);
private:
	//Color values
	int R;
	int G;
	int B;
	int A; //Alpha

};

#endif /* SRC_MODEL_PIXEL_HPP_ */

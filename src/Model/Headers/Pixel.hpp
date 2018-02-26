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
	Pixel(int r, int g, int b);
	Pixel(int r, int g, int b, int a);
	virtual ~Pixel();
	//Getters
	int getRed();
	int getGreen();
	int getBlue();
	int getAlpha();


	//Setters
	void setRed(int r);
	void setGreen(int g);
	void setBlue(int b);
	void setAlpha(int a);
private:
	//Color values
	int r;
	int g;
	int b;
	int a; //Alpha

};

#endif /* SRC_MODEL_PIXEL_HPP_ */

/*
 * Pixel.cpp
 *
 *  Created on: Feb 26, 2018
 *      Author: Derek
 */

#include "Headers/Pixel.hpp"

Pixel::Pixel() {
	this->r = 0;
	this->g = 0;
	this->b = 0;
	this->a = 0;
}

Pixel::Pixel(int r, int g, int b){
	this->r = r;
	this->g = g;
	this->b = b;
	this->a = 255;
}

Pixel::Pixel(int r, int g, int b, int a){
	this->r = r;
	this->g = g;
	this->b = b;
	this->a = a;
}

Pixel::~Pixel() {
	// TODO Auto-generated destructor stub
}


//Getters
int Pixel::getRed(){
	return r;
}

int Pixel::getGreen(){
	return g;
}

int Pixel::getBlue(){
	return b;
}

int Pixel::getAlpha(){
	return a;
}

//Setters
void Pixel::setRed(int r){
	this->r = r;
}
void Pixel::setGreen(int g){
	this->g = g;
}
void Pixel::setBlue(int b){
	this->b = b;
}
void Pixel::setAlpha(int a){
	this->a = a;
}

#include <iostream>
#include <roi_grabber/roi_grabber.h>
#include <opencv2/highgui.hpp>

using namespace std;
using namespace cv;

/*!
 * This is a very simple test for roi_grabber module!
 */
int main(int argc, char * argv[]){
	Mat img = imread("xyz.png");
    if(img.empty()){
        cout << "Cannot read image!" << endl;
        return -1;
    }

	ROIGrabber gr;
	Rect r = gr.GetRoi(img);
    //fill it with white color
	img(r).setTo(Scalar(255,255,255));
	imshow("output", img);
	waitKey();
	cout << "Test Finished Succefully!" << endl;
	return 0;
}

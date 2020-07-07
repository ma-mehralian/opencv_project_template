#include <iostream>
#include <roi_grabber/roi_grabber.h>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>

using namespace std;
using namespace cv;

/*!
 * This is a very complex application which use roi_grabber module!
 */
int main(int argc, char * argv[]){
    Mat img = imread("xyz.png");
    if(img.empty()){
        cout << "Cannot read image!" << endl;
        return -1;
    }

    ROIGrabber gr;
    Rect r = gr.GetRoi(img);
    //fill it nwith white color
    Mat c_out;
    Canny(img(r), c_out, 128, 195);
    img(r).setTo(Scalar(255,255,255), c_out);
    imshow("output", img);
    waitKey();
    cout << "Test Finished Succefully!" << endl;
    return 0;
}

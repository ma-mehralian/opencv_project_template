#include <roi_grabber/roi_grabber.h>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>

using namespace cv;

cv::Rect ROIGrabber::GetRoi(const cv::Mat &img){
	Point start_p(-1,-1), end_p;

	auto on_mouse = [](int event, int x, int y, int, void* data) {
		Mat& img = *static_cast<Mat*>(((void**)data)[0]);
		Point& p_s = *static_cast<Point*>(((void**)data)[1]);
		Point& p_e = *static_cast<Point*>(((void**)data)[2]);

		Mat img_c = img.clone();
		if (p_s.x != -1){
            rectangle(img_c, p_s, Point(x,y), Scalar(0,0,255), 1);
			imshow("ROI_GRABBER", img_c);
		}
		if (event == EVENT_LBUTTONDOWN) {
			if (p_s.x == -1){
				p_s.x = x;
				p_s.y = y;
			}else{
				p_e.x = x;
				p_e.y = y;
				cv::destroyWindow("ROI_GRABBER");
			}
		}
	};


    void* args[] = { const_cast<void*>((const void*)(&img)) , &start_p, &end_p };
    imshow("ROI_GRABBER", img);
    setMouseCallback("ROI_GRABBER", on_mouse, args);
	waitKey();
    return Rect(start_p, end_p);
}

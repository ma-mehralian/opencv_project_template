#ifndef _ROI_GRABBER_H_
#define _ROI_GRABBER_H_

#include <opencv2/core.hpp>

/*!
 * Very simple class
 * \author ma.mehralian ma.mehralin@gmail.com
 */
class ROIGrabber{
public:
	/*!
	 * This function return rect of ROI 
	 * 
	 * /param img input image to select ROI rect
	 * /return ROI rect
	 */
	cv::Rect GetRoi(const cv::Mat &img);
};

#endif //_ROI_GRABBER_H_

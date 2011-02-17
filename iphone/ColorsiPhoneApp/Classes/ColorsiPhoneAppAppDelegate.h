//
//  ColorsiPhoneAppAppDelegate.h
//  ColorsiPhoneApp
//
//  Created by Rich Atkinson on 17/02/11.
//  Copyright Platform46 2011. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "PhoneGapDelegate.h"

@interface ColorsiPhoneAppAppDelegate : PhoneGapDelegate {
	// Database variables 
	NSString *databaseName; 
	NSString *databasePath; 
	NSString *databaseFile; 
	NSString *masterName; 
	NSString *masterPath; 
	NSString *masterFile; 
}

@end


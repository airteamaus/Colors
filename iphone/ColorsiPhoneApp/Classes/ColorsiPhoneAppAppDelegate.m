//
//  ColorsiPhoneAppAppDelegate.m
//  ColorsiPhoneApp
//
//  Created by Rich Atkinson on 17/02/11.
//  Copyright Platform46 2011. All rights reserved.
//

#import "ColorsiPhoneAppAppDelegate.h"
#import "PhoneGapViewController.h"

@implementation ColorsiPhoneAppAppDelegate

- (id) init
{	
	/** If you need to do any extra app-specific initialization, you can do it here
	 *  -jm
	 **/
    return [super init];
}

/**
 * This is main kick off after the app inits, the views and Settings are setup here.
 */
- (void)applicationDidFinishLaunching:(UIApplication *)application
{		
	//Copy over the database if it doesn't exist 
	// Setup some globals 
	databaseName = @"0000000000000001.db"; 
	masterName = @"Databases.db"; 
	// Get the path to the Library directory and append the databaseName 
	NSArray *libraryPaths = NSSearchPathForDirectoriesInDomains (NSLibraryDirectory, NSUserDomainMask, YES); 
	NSString *libraryDir = [libraryPaths objectAtIndex:0]; 
	// the directory path for the Databases.db file 
	masterPath = [libraryDir stringByAppendingPathComponent:@"WebKit/Databases/"]; 
	// the directory path for the 0000000000000001.db file 
	databasePath = [libraryDir stringByAppendingPathComponent:@"WebKit/Databases/file_0/"]; 
	// the full path for the Databases.db file 
	masterFile = [masterPath stringByAppendingPathComponent:masterName]; 
	// the full path for the 0000000000000001.db file 
	databaseFile = [databasePath stringByAppendingPathComponent:databaseName]; 

	// Execute the "checkAndCreateDatabase" function 
	[self checkAndCreateDatabase]; 

	[ super applicationDidFinishLaunching:application ];
}



-(void) checkAndCreateDatabase{ 
	// Check if the SQL database has already been saved to the users phone, if not then copy it over 

	BOOL success; 
	// Create a FileManager object, we will use this to check the status 
	// of the database and to copy it over if required 
	NSFileManager *fileManager = [NSFileManager defaultManager]; 
	
	// Check if the database has already been created in the users filesystem 
	success = [fileManager fileExistsAtPath:databasePath]; 
	
	// If the database already exists then return without doing anything 
	if(success) return; 
	
	// If not then proceed to copy the database from the application to the users filesystem 
	// Get the path to the database in the application package 
	NSString *databasePathFromApp = [[[NSBundle mainBundle] resourcePath] 
									 stringByAppendingPathComponent:databaseName]; 
	NSString *masterPathFromApp = [[[NSBundle mainBundle] resourcePath] 
								   stringByAppendingPathComponent:masterName];
	
	// Create the database folder structure 
	success = [fileManager createDirectoryAtPath:databasePath 
		   withIntermediateDirectories:YES attributes:nil error:NULL]; 
	if(success != YES) NSLog(@"Error");
	
	// Copy the database from the package to the users filesystem 
	success = [fileManager copyItemAtPath:databasePathFromApp toPath:databaseFile error:nil]; 
	if(success != YES) NSLog(@"Error");
	
	// Copy the Databases.db from the package to the appropriate place 
	success = [fileManager copyItemAtPath:masterPathFromApp toPath:masterFile error:nil]; 
	if(success != YES) NSLog(@"Error");
	
	[fileManager release]; 
} 


-(id) getCommandInstance:(NSString*)className
{
	/** You can catch your own commands here, if you wanted to extend the gap: protocol, or add your
	 *  own app specific protocol to it. -jm
	 **/
	return [super getCommandInstance:className];
}

/**
 Called when the webview finishes loading.  This stops the activity view and closes the imageview
 */
- (void)webViewDidFinishLoad:(UIWebView *)theWebView 
{
	return [ super webViewDidFinishLoad:theWebView ];
}

- (void)webViewDidStartLoad:(UIWebView *)theWebView 
{
	return [ super webViewDidStartLoad:theWebView ];
}

/**
 * Fail Loading With Error
 * Error - If the webpage failed to load display an error with the reson.
 */
- (void)webView:(UIWebView *)theWebView didFailLoadWithError:(NSError *)error 
{
	return [ super webView:theWebView didFailLoadWithError:error ];
}

/**
 * Start Loading Request
 * This is where most of the magic happens... We take the request(s) and process the response.
 * From here we can re direct links and other protocalls to different internal methods.
 */
- (BOOL)webView:(UIWebView *)theWebView shouldStartLoadWithRequest:(NSURLRequest *)request navigationType:(UIWebViewNavigationType)navigationType
{
	return [ super webView:theWebView shouldStartLoadWithRequest:request navigationType:navigationType ];
}


- (BOOL) execute:(InvokedUrlCommand*)command
{
	return [ super execute:command];
}

- (void)dealloc
{
	[ super dealloc ];
}

@end

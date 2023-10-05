// swift-tools-version: 5.7
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
	name: "PythonSwiftPackages",
	platforms: [.iOS(.v13)],
	products: [
		// Products define the executables and libraries a package produces, making them visible to other packages.
		.library(name: "PyFoundation", targets: ["PyFoundation"]),
		.library(name: "PyTextToSpeech", targets: ["PyTextToSpeech"]),
		.library(name: "PySpeechRecognizer", targets: ["PySpeechRecognizer"]),
		.library(name: "PyWebViews", targets: ["PyWebViews"]),
		.library(name: "PyCoreBluetooth", targets: ["PyCoreBluetooth"]),
		.library(name: "PyCoreVideo", targets: ["PyCoreVideo"]),
		//.library(name: "PyPHPicker", targets: ["PyPHPicker"]),
		.library(name: "PyCamera", targets: ["PyCamera"]),
		.library(name: "PyAdmob", targets: ["PyAdmob"]),
		
	],
	dependencies: [
		.package(path: "/Volumes/CodeSSD/GitHub/SwiftonizePlugin"), // will be github url later
		.package(path: "../PythonLib"), // required package
		.package(path: "../PythonSwiftCore"), // required package
		.package(url: "https://github.com/googleads/swift-package-manager-google-mobile-ads", branch: "main")
	],
	targets: [
		// Targets are the basic building blocks of a package, defining a module or a test suite.
		// Targets can depend on other targets in this package and products from dependencies.
		.target(
			name: "PyFoundation",
			dependencies: [
				"PythonLib",
				"PythonSwiftCore",
			],
			
			// adding Swiftonize as plugin will make it automatic build all files in "wrappers"
			plugins: [ .plugin(name: "Swiftonize", package: "SwiftonizePlugin") ]
		),
		.target(
			name: "PyTextToSpeech",
			dependencies: [
				"PythonLib",
				"PythonSwiftCore",
			],
			// adding Swiftonize as plugin will make it automatic build all files in "wrappers"
			plugins: [ .plugin(name: "Swiftonize", package: "SwiftonizePlugin") ]
		),
		.target(
			name: "PySpeechRecognizer",
			dependencies: [
				"PythonLib",
				"PythonSwiftCore",
			],
			plugins: [ .plugin(name: "Swiftonize", package: "SwiftonizePlugin") ]
		),
		.target(
			name: "PyWebViews",
			dependencies: [
				"PythonLib",
				"PythonSwiftCore",
			],
			plugins: [ .plugin(name: "Swiftonize", package: "SwiftonizePlugin") ]
		),
		.target(
			name: "PyCoreBluetooth",
			dependencies: [
				"PythonLib",
				"PythonSwiftCore",
			],
			plugins: [ .plugin(name: "Swiftonize", package: "SwiftonizePlugin") ]
		),
		.target(
			name: "PyCoreVideo",
			dependencies: [
				"PythonLib",
				"PythonSwiftCore",
			],
			plugins: [ .plugin(name: "Swiftonize", package: "SwiftonizePlugin") ]
		),
//		.target(
//			name: "PyPHPicker",
//			dependencies: [
//				"PythonLib",
//				"PythonSwiftCore",
//			],
//			plugins: [ .plugin(name: "Swiftonize", package: "SwiftonizePlugin") ]
//		),
		.target(
			name: "PyCamera",
			dependencies: [
				"PythonLib",
				"PythonSwiftCore",
				"PyCoreVideo"
			],
			plugins: [ .plugin(name: "Swiftonize", package: "SwiftonizePlugin") ]
		),
		.target(
			name: "PyAdmob",
			dependencies: [
				"PythonLib",
				"PythonSwiftCore",
				// admob package
				.product(name: "GoogleMobileAds", package: "swift-package-manager-google-mobile-ads")
			],
			plugins: [ .plugin(name: "Swiftonize", package: "SwiftonizePlugin") ]
		),
		
	]
)

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
<<<<<<< Updated upstream
		//.package(path: "/Volumes/CodeSSD/GitHub/SwiftonizePlugin"), // will be github url later
		.package(url: "https://github.com/PythonSwiftLink/SwiftonizePlugin", branch: "master"),
		.package(path: "../PythonLib"), // required package
		.package(path: "../PythonSwiftCore"), // required package
=======
		.package(path: "/Volumes/CodeSSD/GitHub/SwiftonizePlugin"), // will be github url later
		//.package(path: "../PythonLib"), // required package
		.package(path: "../PythonSwiftLink"), // required package
>>>>>>> Stashed changes
		.package(url: "https://github.com/googleads/swift-package-manager-google-mobile-ads", branch: "main")
	],
	targets: [
		// Targets are the basic building blocks of a package, defining a module or a test suite.
		// Targets can depend on other targets in this package and products from dependencies.
		.target(
			name: "PyFoundation",
			dependencies: [
				.product(name: "PythonSwiftCore", package: "PythonSwiftLink")
			],
			// adding Swiftonize as plugin will make it automatic build all files in "wrappers"
			plugins: [ .plugin(name: "Swiftonize", package: "SwiftonizePlugin") ]
		),
		.target(
			name: "PyTextToSpeech",
			dependencies: [
				.product(name: "PythonSwiftCore", package: "PythonSwiftLink")
			],
			// adding Swiftonize as plugin will make it automatic build all files in "wrappers"
			plugins: [ .plugin(name: "Swiftonize", package: "SwiftonizePlugin") ]
		),
		.target(
			name: "PySpeechRecognizer",
			dependencies: [
				.product(name: "PythonSwiftCore", package: "PythonSwiftLink"),
			],
			plugins: [ .plugin(name: "Swiftonize", package: "SwiftonizePlugin") ]
		),
		.target(
			name: "PyWebViews",
			dependencies: [
				.product(name: "PythonSwiftCore", package: "PythonSwiftLink")
			],
			plugins: [ .plugin(name: "Swiftonize", package: "SwiftonizePlugin") ]
		),
		.target(
			name: "PyCoreBluetooth",
			dependencies: [
				.product(name: "PythonSwiftCore", package: "PythonSwiftLink")
			],
			resources: [.copy("example")],
			plugins: [ .plugin(name: "Swiftonize", package: "SwiftonizePlugin") ]
		),
		.target(
			name: "PyCoreVideo",
			dependencies: [
				.product(name: "PythonSwiftCore", package: "PythonSwiftLink")
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
				.product(name: "PythonSwiftCore", package: "PythonSwiftLink"),
				"PyCoreVideo",
			],
			plugins: [ .plugin(name: "Swiftonize", package: "SwiftonizePlugin") ]
		),
		.target(
			name: "PyAdmob",
			dependencies: [
				.product(name: "PythonSwiftCore", package: "PythonSwiftLink"),
				// admob package
				.product(name: "GoogleMobileAds", package: "swift-package-manager-google-mobile-ads")
			],
			plugins: [ .plugin(name: "Swiftonize", package: "SwiftonizePlugin") ]
		),
		
	]
)

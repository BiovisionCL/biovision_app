
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});
  
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Biovision Web Test',
      home: Scaffold(
        appBar: AppBar(title: const Text('Biovision Web Test')),
        body: const Center(child: Text('Flutter Web Running')),
      ),
    );
  }
}

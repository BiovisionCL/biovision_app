
import 'package:flutter/material.dart';
import 'theme.dart';

void main() {
  runApp(const BiovisionApp());
}

class BiovisionApp extends StatelessWidget {
  const BiovisionApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Biovision',
      theme: appTheme,
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Biovision Premium'),
        ),
        body: const Center(
          child: Text('Bienvenido a Biovision', style: TextStyle(fontSize: 24)),
        ),
      ),
    );
  }
}

import 'package:flutter/material.dart';
import 'theme.dart';

void main() {
  runApp(BiovisionApp());
}

class BiovisionApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Biovision',
      theme: appTheme,
      home: Scaffold(
        appBar: AppBar(title: Text('Biovision Premium')),
        body: Center(child: Text('Bienvenido a Biovision', style: Theme.of(context).textTheme.titleLarge)),
      ),
    );
  }
}

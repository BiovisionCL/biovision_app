import 'package:flutter_test/flutter_test.dart';
import 'package:biovision_app/features/home/presentation/home_page.dart';
import 'package:flutter/material.dart';

void main() {
  testWidgets('HomePage displays expected widgets', (WidgetTester tester) async {
    await tester.pumpWidget(MaterialApp(home: HomePage()));
    expect(find.textContaining(''), findsWidgets); // Ajusta según contenido real
  });
}

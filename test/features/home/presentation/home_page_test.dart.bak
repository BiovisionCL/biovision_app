import 'package:flutter_test/flutter_test.dart';
import 'package:flutter/material.dart';
import 'package:biovision_app/features/home/presentation/home_page.dart';

void main() {
  testWidgets('HomePage renders and button works', (WidgetTester tester) async {
    await tester.pumpWidget(const MaterialApp(home: HomePage()));

    expect(find.text('Presióname'), findsOneWidget);

    await tester.tap(find.text('Presióname'));
    await tester.pump();
  });
}
